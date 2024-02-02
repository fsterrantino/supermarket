SELECT * FROM supermarket_products;
SELECT * FROM supermarket_prices;

SELECT count(*) FROM supermarket_products;
SELECT count(*) FROM supermarket_prices;

DELETE FROM supermarket_products;
DELETE FROM supermarket_prices;

WITH products_with_more_than_one_price AS (
	SELECT sku, count(sku) 
	FROM supermarket_prices
	GROUP BY sku
	HAVING count(sku) > 1
),
prices_changes AS (
	SELECT
		sp.sku,
		pr.product_brand,
		pr.product_description,
		final_price,
		final_price - LAG(final_price) OVER (PARTITION BY sp.sku ORDER BY sp.timestamp ASC) AS price_change,
		((final_price - LAG(final_price) OVER (PARTITION BY sp.sku ORDER BY sp.timestamp ASC)) / (LAG(final_price) OVER (PARTITION BY sp.sku ORDER BY sp.timestamp ASC)) * 100)::numeric(5,2) || '%' AS price_change_percentage,
		sp.timestamp
	FROM supermarket_prices sp
		JOIN products_with_more_than_one_price pp
			ON sp.sku = pp.sku
		JOIN supermarket_products pr
			ON pr.sku = sp.sku
	ORDER BY sku, timestamp ASC
)
SELECT *
FROM prices_changes
WHERE price_change IS NOT NULL
ORDER BY CAST(REPLACE(price_change_percentage, '%', '') AS FLOAT) ASC
LIMIT 10
;

