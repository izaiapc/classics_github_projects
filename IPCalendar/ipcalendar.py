<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calendário Interativo</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>

<div id="calendar">
  <div class="header">
    <button id="prevYearBtn">◄</button>
    <button id="prevMonthBtn">◄</button>
    <h2 id="currentMonth"></h2>
    <button id="nextMonthBtn">►</button>
    <button id="nextYearBtn">►</button>
  </div>
  <div class="weekdays">
    <div>Sun</div>
    <div>Mon</div>
    <div>Tue</div>
    <div>Wed</div>
    <div>Thu</div>
    <div>Fri</div>
    <div>Sat</div>
  </div>
  <div class="days"></div>
</div>

<script src="script.js"></script>
</body>
</html>

