function formatDate(d){
    d = new Date(d);
    return (d.getFullYear())+'-'+(d.getMonth()+1)+'-'+(d.getDate());
}
function formatDateTime(d){
    d = new Date(d);
    d.setTime( d.getTime() + d.getTimezoneOffset()*60*1000 );
    return (d.getFullYear())+'-'+(d.getMonth()+1)+'-'+(d.getDate()+'-'+
        d.getHours()+':'+d.getMinutes()+':'+d.getSeconds());
}

function updateEvent(event, delta, revertFunc) {
    if (event.type == 0 || (event.type != 0 && confirm("Update all event repeat?"))){
        if (!confirm("is this okay?")) {
            revertFunc();
        }else{
            $.ajax({
                url: "/admin/fullcalendar/update_event",
                type: "POST",
                dataType: "json",
                data: ({
                    event_id: event.id,
                    end_time:  formatDateTime(event.end),
                    start_time: formatDateTime(event.start),
                }),
                success: function(data) {
                    $('#alert_fullcalendar').html('<div class="alert alert-success">Course '+
                        data+' is changed</div>');
                    setTimeout(function() {
                        $('.alert').fadeOut('normal');
                      }, 2000);
                },
                error: function() {
                  revertFunc();
                }
            });
        }
    } else {
        alert('update only one event in repeat event');
    }
}

$(document).ready(function() {
    var pathname = window.location.pathname.split( '/' );
    var student_id = pathname[pathname.length-1];
    d = new Date();
    var string_date = formatDate(d);
    $('#calendar_student').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay,listWeek'
        },
        defaultDate: string_date,
        navLinks: true, // can click day/week names to navigate views
        editable: false,
        displayEventEnd: true,
        timeFormat: 'H(:mm)',
        eventLimit: true, // allow "more" link when too many events
        timezone: 'Asia/Bangkok',
        viewRender: function(view, element) {
            var moment = $('#calendar_student').fullCalendar('getDate');
            d = new Date(moment);
            var string_date =  formatDate(d);
            $.ajax({
                url: "/student/eventfeeds",
                type: "POST",
                data: {
                    student_id: student_id,
                    default_date: string_date,
                },
                success: function(data) {
                    $('#calendar_student').fullCalendar('refetchEvents');
                    $('#calendar_student').fullCalendar('renderEvents', data);
                }
            });
        },
    });
});

$(document).ready(function() {
    var pathname = window.location.pathname.split( '/' );
    var student_id = pathname[pathname.length-1];
    d = new Date();
    var string_date = formatDate(d);
    $('#calendar_admin').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay,listWeek'
        },
        defaultDate: string_date,
        navLinks: true, // can click day/week names to navigate views
        editable: true,
        displayEventEnd: true,
        timeFormat: 'H(:mm)',
        eventLimit: true, // allow "more" link when too many events
        timezone: 'Asia/Bangkok',
        viewRender: function(view, element) {
            var moment = $('#calendar_admin').fullCalendar('getDate');
            d = new Date(moment);
            var string_date =  formatDate(d);
            $.ajax({
                url: "/admin/course/eventfeeds",
                type: "POST",
                data: {
                    student_id: student_id,
                    default_date: string_date,
                },
                success: function(data) {
                    $('#calendar_admin').fullCalendar('refetchEvents');
                    $('#calendar_admin').fullCalendar('renderEvents', data);
                }
            });
        },
        // resize event, change end time of event
        eventResize: function(event, delta, revertFunc) {
            updateEvent(event, delta, revertFunc);
        },
        // drag event
        eventDrop: function(event, delta, revertFunc) {
            updateEvent(event, delta, revertFunc);
        },
    });
});

//$(document).on('click', '.fc-next-button', function () {
//    var moment = $('#calendar').fullCalendar('getDate');
//    alert(moment);
//    var pathname = window.location.pathname.split( '/' );
//    var student_id = pathname[pathname.length-1];
//    d = new Date(moment);
//    var string_date = (d.getFullYear())+'-'+(d.getMonth()+1)+'-'+(d.getDate())
//    alert(string_date);
//    $('#calendar').fullCalendar({
//        header: {
//            left: 'prev,next today',
//            center: 'title',
//            right: 'month,agendaWeek,agendaDay,listWeek'
//        },
//        defaultDate: string_date,
//        navLinks: true, // can click day/week names to navigate views
//        editable: false,
//        eventLimit: true, // allow "more" link when too many events
//        events: {
//            url: "/student/eventfeeds",
//            type: "POST",
//            data: {
//                student_id: student_id,
//                default_date: string_date,
//            },
//        },
//        timezone: 'Asia/Bangkok'
//    });
//});
//$(document).on('click', '.fc-next-button', function () {
//    $('#calendar').fullCalendar('refetchEvents');
//});
