$(document).ready(function(){
  $("#myMenu li").click(function() {
    $("#myMenu li").removeClass("current");
    $(this).addClass("current");
  });

  $("#logo").click(function () {
    $("#myMenu li").removeClass("current");
  });
});