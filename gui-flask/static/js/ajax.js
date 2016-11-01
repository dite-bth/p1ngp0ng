$( document ).ready(function() {

var rootUrl = '';

(function worker() {

  $.ajax({
    cache: false,
    //url: '../wu15/me1580/pingponghack/TeamMasse/info.txt', 
    url: 'js/profile.js', 
    success: function(data) {
        var newData = $.parseJSON(data);
        /*var newerData = newData.sort(function(a,b){
            return b.points-a.points;
        });*/
        
        
        $(newData).each(function(i){
            $('#scoreViewOne').html(newData[0].Bluepoints);
            
            $('#scoreViewTwo').html(newData[0].Redpoints);
 
            $('.setPoint.setLeft.'+newData[0].Redset).addClass('wonPoint');
            $('.setPoint.setRight.'+newData[0].Blueset).addClass('wonPoint');
            

            if (newData[0].Blueset == 0 && newData[0].Redset == 0) {
                $('.setPoint.setRight').removeClass('wonPoint');
                $('.setPoint.setLeft').removeClass('wonPoint');
            }    
            
                
            
            //console.log(newData[0].Blueset)

            
           
        });
    },
    error: function(err) {
        
    },
    complete: function() {
      // Schedule the next request when the current one's complete
      setTimeout(worker, 1000);
    }
  });
})();
});

