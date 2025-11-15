SELECT 
    a.mac,
    COUNT(*) AS salts
FROM accounts a
JOIN encryptions e ON a.id = e.account_id
WHERE e.is_active = 1
    AND CHAR_LENGTH(e.salt) < 8
GROUP BY a.mac
ORDER BY a.mac;