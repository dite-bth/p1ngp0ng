 $(document).ready(function() {
    $(".servBall").animate ({ "marginTop": "+=3px" }, "slow" );
 function loop() {
    $(".servBall").animate ({ "marginTop": "+=10px" }, "slow" );
    $(".servBall").animate ({ "marginTop": "-=10px" }, "slow" );
    $(".slidingPanelOne").animate ({ "marginTop": "+=270px" }, 2800 );
    $(".slidingPanelOne").animate ({ "marginTop": "-=270px" }, 2800 );
    $(".slidingPanelTwo").animate ({ "marginTop": "-=270px" }, 2800 );
    $(".slidingPanelTwo").animate ({ "marginTop": "+=270px" }, 2800 );



    loop();
    }
        
    loop();


 });





