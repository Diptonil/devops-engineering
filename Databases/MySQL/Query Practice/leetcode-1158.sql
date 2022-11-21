-- https://leetcode.com/problems/market-analysis-i/

SELECT Users.user_id AS buyer_id,
       Users.join_date,
       IFNULL(COUNT(Orders.order_date), 0) AS orders_in_2019
  FROM Users
  LEFT JOIN Orders ON Users.user_id = Orders.buyer_id
            AND YEAR(Orders.order_date) = '2019'
  GROUP BY Users.user_id;