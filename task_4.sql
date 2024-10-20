-- Script: task_4.sql
-- Description: Prints the full description of the Books table from the specified database

SELECT 
    COLUMN_NAME AS 'Column',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Null',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx-book_store'
    AND TABLE_NAME = 'Books';
