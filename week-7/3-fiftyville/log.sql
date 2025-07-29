-- Keep a log of any SQL queries you execute as you solve the mystery.


--Find crime scene report of stolen CS50 duck
SELECT description
FROM crime_scene_reports
WHERE day = 28 AND year = 2021
AND street = "Humphrey Street";
--Took place at 10:15am at bakery
--3 witness, present at the time; all mention bakery


--Find clues from interviews
SELECT name, transcript
FROM interviews
WHERE day = 28 AND month = 7
AND year = 2021;
--Ruth: Within 10 minutes of theft, thief gets into car in bakery parking lot (check security footage)
--Eugene: Earlier the morning, before arrive at bakery, saw thief withdrawing from Leggett Street ATM
--Raymond: After thief left bakery, thief called for < 1 min, earliest flight out of Fiftyville tomorrow, person other end purchase ticket


--Witness Ruth
SELECT *
FROM bakery_security_logs
WHERE year - 2021 AND month = 7
AND day = 28 AND hour = 10
AND minute BETWEEN 10 AND 25;
--Check license plates
SELECT p.name, bsl.activity, bsl.license_plate, bsl.year, bsl.month, bsl.day, bsl.hour, bsl.minute
FROM bakery_security_logs bsl
JOIN people p on p.license_plate = bsl.license_plate
WHERE bsl.year = 2021 AND bsl.month = 7
AND bsl.day = 28 AND bsl.hour = 10
AND bsl.minute BETWEEN 15 AND 25;

--Witness Eugene
SELECT *
FROM atm_transactions
WHERE atm_location = "Leggett Streeet"
AND year = 2021 AND month = 7 AND day = 28;
--Add name to withdraws
SELECT a.*, p.name
FROM atm_transactions a
JOIN bank_accounts b ON a.account_number = b.account_number
JOIN people p ON b.person_id = p.id
WHERE a.atm_location = "Leggett Street" AND a.year = 2021 AND a.month = 7
AND a.day = 28 AND a.transaction_type = "withdraw";

--Witness Raymond
SELECT *
FROM phone_calls
WHERE year = 2021 AND month = 7
AND day = 28 AND duration < 60;
--Add names to callers
SELECT p.name, pc.caller, pc.receiver, pc.year, pc.month, pc.day, pc.duration
FROM phone_calls pc
JOIN people p ON pc.caller = p.phone_number
WHERE pc.year = 2021 AND pc.month = 7
AND pc.day = 28 AND pc.duration < 60;
--Explore airport
SELECT *
FROM airports;
--Fiftyville id 8 explore flights
SELECT f.*, origin.full_name AS origin_airport, destination.full_name AS destination_airport
FROM flights f
JOIN airports origin ON f.origin_airport_id = origin.id
JOIN airports destination ON f.destination_airport_id = destination.id
WHERE origin.id = 8 AND f.year = 2021 AND f.month = 7
AND f.day = 29
ORDER BY f.hour, f.minute;

--Combine all clues
SELECT p.name
FROM bakery_security_logs bsl
JOIN people p ON p.license_plate = bsl.license_plate
JOIN bank_accounts ba ON ba.person_id = p.id
JOIN atm_transactions at ON at.account_number = ba.account_number
JOIN phone_calls pc ON pc.caller = p.phone_number
WHERE bsl.year = 2021 AND bsl.month = 7 AND bsl.day = 28 AND bsl.hour = 10
AND bsl.minute BETWEEN 15 AND 25 AND at.atm_location = "Leggett Street" AND at.year = 2021 AND at.month = 7
AND at.transaction_type = "withdraw" AND at.day = 28 AND pc.year = 2021 AND pc.month = 7
AND pc.day = 28 AND pc.duration < 60;
--Narrow down from Diana/Bruce on flight
SELECT p.name
FROM people p
JOIN passengers ps ON p.passport_number = ps.passport_number
WHERE ps.flight_id = 36
AND p.name IN ("Bruce", "Diana");
--Bruce is the thief

--Bruce called
SELECT p2.name AS receiver
FROM phone_calls pc
JOIN people p1 ON pc.caller = p1.phone_number
JOIN people p2 ON pc.receiver = p2.phone_number
WHERE p1.name = "Bruce" AND pc.year = 2021 AND pc.month = 7
AND pc.day = 28 AND pc.duration < 60;
--Robin was the helper


