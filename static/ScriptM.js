$(document).ready(function() {
	
	var answers = [0,3,0,1,2];
	var count = 0;
	var questions = [];
	var rightCount = 0;
	var buttonclicked = false;
	var answer = -1
	
	//question 1 stuff
	
	$("#a").click(function() {
		$("p").css("border-style","none");
		$("#a").css("border-style","solid");
		answer = 0;
	});	
	$("#b").click(function() {
		$("p").css("border-style","none");
		$("#b").css("border-style","solid");
		answer = 1;
	});	
	$("#c").click(function() {
		$("p").css("border-style","none");
		$("#c").css("border-style","solid");
		answer = 2;
	});	
	$("#d").click(function() {
		$("p").css("border-style","none");
		$("#d").css("border-style","solid");
		answer = 3;
	});	
	
	
	$("#next").click(function() {
		if (answers[count] == answer && answer!= -1) {
			rightCount+=1;
			//do some sort of animation
			$("body").css("background-color","green");
			$("#ani").text("correct!");
			$("#ani").animate({opacity: 1.0},"slow");
			$("#ani").animate({opacity: 0.0},"slow");
		}
		else {
			$("body").css("background-color","red");
			$("#ani").text("wrong!");
			$("#ani").animate({opacity: 1.0},"slow");
			$("#ani").animate({opacity: 0.0},"slow");
		}
		
		count+=1
		if (count == 1) {
			$("#q1").text("Which of the following is considered a special property that applies to only a few minerals?");
			$("#a").text("Color");
			$("#b").text("Luster");
			$("#c").text("Streak");
			$("#d").text("Magnetism");
			
			
		}
		if (count == 2) {
			$("#q1").text("A mineral fizzes when a weak acid is dropped on it, the mineral is probably");
			$("#a").text("Halite");
			$("#b").text("Magnetite");
			$("#c").text("Calcite");
			$("#d").text("Quartz");
		
		}
		if (count == 3) {
			$("#q1").text("Which of the following is is the least hardest based on Moh's test?");
			$("#a").text("Apatite");
			$("#b").text("Talc");
			$("#c").text("Gypsum");
			$("#d").text("Diamond");
		}
		if (count == 4) {
			$("#q1").text("Hardness is a property that helps identify minerals. Scientists use a scale of 1-10 to show the hardness of a mineral. What number would be given to the hardest?");
			$("#a").text("5");
			$("#b").text("1");
			$("#c").text("10");
			$("#d").text("0");
		}
		if (count == 5) { 
			//var txt = "you got: " + String(rightCount) + " out of " + String(count)
			$("#q1").text("You got: " + String(rightCount) +" out of " + String(count) + " correct");
			$("#a").hide();
			$("#b").hide();
			$("#c").hide();
			$("#d").hide();
		}
		answer = -1; 
		$("p").css("border-style","none");
		
	});
	//hello there
});	
	
