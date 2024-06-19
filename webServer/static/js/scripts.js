// 달력 업데이트 함수
function updateCalendar() {
    var year = document.getElementById('calendar-year').value;
    var month = document.getElementById('calendar-month').value;
    var daysInMonth = new Date(year, month, 0).getDate();
    var calendarDiv = document.getElementById('calendar');
    var calendarContent = '';

    // 해당 월의 첫 날의 요일 구하기 (0: 일요일, 1: 월요일, ..., 6: 토요일)
    var firstDayOfWeek = new Date(year, month - 1, 1).getDay();

    // 달력에 표시되는 날짜들 생성
    calendarContent += '<div class="calendar-header">';
    calendarContent += '<div class="calendar-day">일</div>';
    calendarContent += '<div class="calendar-day">월</div>';
    calendarContent += '<div class="calendar-day">화</div>';
    calendarContent += '<div class="calendar-day">수</div>';
    calendarContent += '<div class="calendar-day">목</div>';
    calendarContent += '<div class="calendar-day">금</div>';
    calendarContent += '<div class="calendar-day">토</div>';
    calendarContent += '</div>';
    
    for (var i = 0; i < firstDayOfWeek; i++) {
        calendarContent += '<div class="calendar-day empty"></div>';
    }

    for (var i = 1; i <= daysInMonth; i++) {
        calendarContent += '<button class="calendar-day" onclick="showLogForm(' + i + ')">' + i + '</button>';
        if ((firstDayOfWeek + i) % 7 == 0) {
            calendarContent += '<br>'; // 주말마다 줄 바꿈
        }
    }

    calendarDiv.innerHTML = calendarContent;
}

// 일지 작성 폼 보이기 함수
function showLogForm(day) {
    // 일지 작성 버튼 보이기
    document.getElementById('write-log-button').style.display = 'block';

    // 오늘의 날짜 가져오기
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; // 1월이 0으로 시작하므로 1을 더해줍니다.
    var yyyy = today.getFullYear();

    // 일지 작성 폼의 날짜 필드에 오늘의 날짜 설정
    document.getElementById('log-date').value = yyyy + '-' + mm + '-' + day;
}

// 초기에 달력 업데이트
updateCalendar();
