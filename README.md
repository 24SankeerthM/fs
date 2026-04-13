
Consider the following schema for a Library Database:
BOOK (Book_id, Title, Publisher_Name, Pub_Year)

BOOK_AUTHORS (Book_id, Author_Name)

PUBLISHER (Name, Address, Phone)

BOOK_COPIES (Book_id, Branch_id, No-of_Copies)

BOOK_LENDING (Book_id, Branch_id, Card_No, Date_Out, Due_Date)

LIBRARY_PROGRAMME (Programme_id, Programme_Name, Address)

Write SQL queries to


Retrieve details of all books in the library – id, title, name of publisher, authors, number of copies in each branch, etc.

Get the particulars of borrowers who have borrowed more than 3 books, but from Jan 2017 to Jun 2017

Delete a book in BOOK table. Update the contents of other tables to reflect this data manipulation operation.

Partition the BOOK table based on year of publication. Demonstrate its working with a simple query.


Solution:

Entity-Relationship Diagram








Table Creation

CREATE TABLE PUBLISHER

(NAME VARCHAR2 (20) PRIMARY KEY,

PHONE INTEGER,

ADDRESS VARCHAR2 (20));

CREATE TABLE BOOK

(BOOK_ID INTEGER PRIMARY KEY,

TITLE VARCHAR2 (20),
PUB_YEAR VARCHAR2 (20),

PUBLISHER_NAME REFERENCES PUBLISHER (NAME) ON DELETE CASCADE);

create table book_authors
(author_name varchar2 (20),

book_id references book (book_id) on delete cascade, primary key (book_id, author_name));

create table library_branch

(programme_id integer primary key not null,

programme_name varchar2 (50),

address varchar2 (50));

create table book_copies

(no_of_copies integer,

book_id references book (book_id) on delete cascade,

branch_id references library_branch (branch_id) on delete cascade,

primary key (book_id, branch_id));

create table card

(card_no integer primary key);

create table book_lending

(date_out date,

due_date date,

book_id references book (book_id) on delete cascade,

branch_id references library_branch (branch_id) on delete cascade,

card_no references card (card_no) on delete cascade, primary key (book_id, branch_id, card_no));


Table Descriptions


































Insertion of Values to Tables

INSERT INTO PUBLISHER VALUES (‘MCGRAW-HILL’, 9989076587, ‘BANGALORE’);

INSERT INTO PUBLISHER VALUES (‘PEARSON’, 9889076565, ‘NEWDELHI’);

INSERT INTO PUBLISHER VALUES (‘RANDOM HOUSE’, 7455679345, ‘HYDRABAD’);

INSERT INTO PUBLISHER VALUES (‘HACHETTE LIVRE’, 8970862340, ‘CHENAI’);

INSERT INTO PUBLISHER VALUES (‘GRUPO PLANETA’, 7756120238, ‘BANGALORE’);

INSERT INTO BOOK VALUES (1,’DBMS’,’JAN-2017’, ‘MCGRAW-HILL’); INSERT INTO BOOK VALUES (2,’ADBMS’,’JUN-2016’, ‘MCGRAW-HILL’); INSERT INTO BOOK VALUES (3,’CN’,’SEP-2016’, ‘PEARSON’);

INSERT INTO BOOK VALUES (4,’CG’,’SEP-2015’, ‘GRUPO PLANETA’); INSERT INTO BOOK VALUES (5,’OS’,’MAY-2016’, ‘PEARSON’);


INSERT INTO BOOK_AUTHORS VALUES (’NAVATHE’, 1); INSERT INTO BOOK_AUTHORS VALUES (’NAVATHE’, 2);

INSERT INTO BOOK_AUTHORS VALUES (’TANENBAUM’, 3); INSERT INTO BOOK_AUTHORS VALUES (’EDWARD ANGEL’, );
 INSERT INTO BOOK_AUTHORS VALUES (’GALVIN’, 5);

INSERT INTO LIBRARY_PROGRAMME VALUES (10,’RR NAGAR’,’BANGALORE’);

INSERT INTO LIBRARY_PROGRAMME VALUES (11,’RNSIT’,’BANGALORE’);

INSERT INTO LIBRARY_PROGRAMME VALUES (12,’RAJAJI NAGAR’, ’BANGALORE’);

INSERT INTO LIBRARY_PROGRAMME VALUES (13,’NITTE’,’MANGALORE’);

INSERT INTO LIBRARY_PROGRAMME VALUES (14,’MANIPAL’,’UDUPI’);
INSERT INTO LIBRARY_BRANCH VALUES (14,’MANIPAL’,’UDUPI’);

INSERT INTO BOOK_COPIES VALUES (10, 1, 10);

INSERT INTO BOOK_COPIES VALUES (5, 1, 11);

INSERT INTO BOOK_COPIES VALUES (2, 2, 12);

INSERT INTO BOOK_COPIES VALUES (5, 2, 13);

INSERT INTO BOOK_COPIES VALUES (7, 3, 14);

INSERT INTO BOOK_COPIES VALUES (1, 5, 10);

INSERT INTO BOOK_COPIES VALUES (3, 4, 11);

INSERT INTO CARD VALUES (100);

INSERT INTO CARD VALUES (101);

INSERT INTO CARD VALUES (102);

INSERT INTO CARD VALUES (103);

INSERT INTO CARD VALUES (104);


INSERT INTO BOOK_LENDING VALUES (’01-JAN-17’,’01-JUN-17’, 1, 10, 101);

INSERT INTO BOOK_LENDING VALUES (’11-JAN-17’,’11-MAR-17’, 3, 14, 101);

INSERT INTO BOOK_LENDING VALUES (’21-FEB-17’,’21-APR-17’, 2, 13, 101);

INSERT INTO BOOK_LENDING VALUES (’15-MAR-17’,’15-JUL-17’, 4, 11, 101);

INSERT INTO BOOK_LENDING VALUES (‘12-APR-17’,’12-MAY-17’, 1, 11, 104);

SELECT * FROM PUBLISHER;







































Queries:

Retrieve details of all books in the library – id, title, name of publisher, authors, number of copies in each branch, etc.

SELECT B.BOOK_ID, B.TITLE, B.PUBLISHER_NAME, A.AUTHOR_NAME, 
C.NO_OF_COPIES, L.BRANCH_ID

FROM BOOK B, BOOK_AUTHORS A, BOOK_COPIES C, LIBRARY_BRANCH L WHERE B.BOOK_ID=A.BOOK_ID

AND B.BOOK_ID=C.BOOK_ID

AND L.BRANCH_ID=C.BRANCH_ID;



Get the particulars of borrowers who have borrowed more than 3 books, but from Jan 2017 to Jun 2017.

SELECT CARD_NO FROM BOOK_LENDING
WHERE DATE_OUT BETWEEN ’01-JAN-2017’ AND ’01-JUL-2017’

GROUP BY CARD_NO HAVING COUNT (*)>3;





Delete a book in BOOK table. Update the contents of other tables to reflect this data manipulation operation.


DELETE FROM BOOK

WHERE BOOK_ID=3;




















Partition the BOOK table based on year of publication. Demonstrate its working with a simple query.

CREATE VIEW V_PUBLICATION AS

SELECT PUB_YEAR

FROM BOOK;



2.Consider the following schema for Order Database:

SALESMAN (Salesman_id, Name, City, Commission)
CUSTOMER (Customer_id, Cust_Name, City, Grade, Salesman_id) ORDERS (Ord_No, Purchase_Amt, Ord_Date, Customer_id, Salesman_id) Write SQL queries to

Count the customers with grades above Bangalore’s average.

Find the name and numbers of all salesmen who had more than one customer.

List all salesmen and indicate those who have and don’t have customers in their cities

(Use UNION operation.)

Create a view that finds the salesman who has the customer with the highest order of a day.

Solution:

Entity-Relationship Diagram





















Schema Diagram









Table Creation

CREATE TABLE SALESMAN
(SALESMAN_ID NUMBER (4),
NAME VARCHAR2 (20),

CITY VARCHAR2 (20),

COMMISSION VARCHAR2 (20),

PRIMARY KEY(SALESMAN_ID));

CREATE TABLE CUSTOMER1

(CUSTOMER_ID NUMBER (4),

CUST_NAME VARCHAR2 (20),

CITY VARCHAR2 (20),

GRADE NUMBER (3),

PRIMARY KEY (CUSTOMER_ID),

SALESMAN_ID REFERENCES SALESMAN (SALESMAN_ID) ON DELETE SET NULL);

CREATE TABLE ORDERS

(ORD_NO NUMBER (5),

PURCHASE_AMT NUMBER (10, 2),

ORD_DATE DATE,

PRIMARY KEY (ORD_NO),

CUSTOMER_ID REFERENCES CUSTOMER1 (CUSTOMER_ID) ON DELETE CASCADE, SALESMAN_ID REFERENCES SALESMAN (SALESMAN_ID) ON DELETE CASCADE);

Table Descriptions
































Insertion of Values to Tables

INSERT INTO SALESMAN VALUES (1000, ‘JOHN’,’BANGALORE’,’25 %’);

INSERT INTO SALESMAN VALUES (2000, ‘RAVI’,’BANGALORE’,’20 %’);

INSERT INTO SALESMAN VALUES (3000, ‘KUMAR’,’MYSORE’,’15 %’);

INSERT INTO SALESMAN VALUES (4000, ‘SMITH’,’DELHI’,’30 %’);

INSERT INTO SALESMAN VALUES (5000, ‘HARSHA’,’HYDRABAD’,’15 %’);

INSERT INTO CUSTOMER1 VALUES (10, ‘PREETHI’,’BANGALORE’, 100, 1000);

INSERT INTO CUSTOMER1 VALUES (11, ‘VIVEK’,’MANGALORE’, 300, 1000);

INSERT INTO CUSTOMER1 VALUES (12, ‘BHASKAR’,’CHENNAI’, 400, 2000);

INSERT INTO CUSTOMER1 VALUES (13, ‘CHETHAN’,’BANGALORE’, 200, 2000);

INSERT INTO CUSTOMER1 VALUES (14, ‘MAMATHA’,’BANGALORE’, 400, 3000);

INSERT INTO ORDERS VALUES (50, 5000, ‘04-MAY-17’, 10, 1000); INSERT INTO ORDERS VALUES (51, 450, ‘20-JAN-17’, 10, 2000);
INSERT INTO ORDERS VALUES (52, 1000, ‘24-FEB-17’, 13, 2000);

INSERT INTO ORDERS VALUES (53, 3500, ‘13-APR-17’, 14, 3000);

INSERT INTO ORDERS VALUES (54, 550, ‘09-MAR-17’, 12, 2000);


SELECT * FROM SALESMAN;












SELECT * FROM CUSTOMER1;









SELECT * FROM ORDERS;










Queries:

Count the customers with grades above Bangalore’s average.

SELECT GRADE, COUNT (DISTINCT CUSTOMER_ID) FROM CUSTOMER1

GROUP BY GRADE

HAVING GRADE > (SELECT AVG(GRADE) FROM CUSTOMER1

WHERE CITY='BANGALORE');









Find the name and numbers of all salesmen who had more than one customer.

SELECT SALESMAN_ID, NAME FROM SALESMAN A

WHERE 1 < (SELECT COUNT (*)

FROM CUSTOMER1

WHERE SALESMAN_ID=A.SALESMAN_ID);






List all salesmen and indicate those who have and don’t have customers in their cities (Use UNION operation.)

SELECT SALESMAN.SALESMAN_ID, NAME, CUST_NAME,COMMISSION
FROM SALESMAN, CUSTOMER1 C

WHERE SALESMAN.CITY =   C.CITY 
UNION

SELECT SALESMAN_ID, NAME, 'NO MATCH',COMMISSION FROM SALESMAN
WHERE NOT CITY = ANY (SELECT CITY
FROMCUSTOMER1) 
ORDER BY 2 DESC;
















Create a view that finds the salesman who has the customer with the highest order of a day.
CREATE VIEW ELITSALESMAN AS

SELECT B.ORD_DATE,A.SALESMAN_ID,A.NAME       FROM SALESMAN A, ORDERS B
WHERE A.SALESMAN_ID = B.SALESMAN_ID

ANDB.PURCHASE_AMT=(SELECT MAX (PURCHASE_AMT)

FROM ORDERS C

WHERE C.ORD_DATE = B.ORD_DATE);


