// Enable pusher logging - don't include this in production
Pusher.logToConsole = true;

var pusher = new Pusher('15e72d442d16f43e033c', {
  cluster: 'ap1',
  encrypted: true
});

var channel = pusher.subscribe('my-channel');
channel.bind('my-event', function(data) {
    $('#activity').prepend( "<tr><td>"+data.user_name+" "+data.action+
    " "+data.object_type+" "+data.object_name+"</td><td>"+data.time+"</td></tr>");
    if(data.object_type_es == 'course' && data.action_es == 'delete'){
        $('#course-'+data.object_id).remove();
    }
});