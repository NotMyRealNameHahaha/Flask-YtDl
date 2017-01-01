/*
Created by Chris, AKA NotMyRealNameHahaha

This file is licensed under the DO WHAT THE FUCK YOU WANT TO public license
The original license was created by Github user ajalt:  https://github.com/ajalt

The backend of this application was heavily influenced by FuckIt, thus it uses the same license.


---------------------------------------------------------
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2014

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.
 */



(function() {
    // Easy toggle function
    function kTog(which, what) {
        document.getElementById(which).classList.toggle(what);
    }


    // Toggle function w/ event target
    function evtkTog(evt, evtKlass, which, what) {
        document.getElementById(which).classList.toggle(what);
        evt.currentTarget.classList.add(evtKlass);
    }

    // Reveal the hidden input fields
    document.getElementById("more_inputs").onclick = function(){
        // Remove class "hidden"
        kTog("hider", "hidden");
        // Add border to first input field
        kTog("main_input", "b-no");
        // Do a magic trick
        this.parentNode.removeChild(this);
        // Grammars
        document.getElementById("get_music").innerHTML = "Get songs";
    };

    // Parse JSON response.
    // Example response: { 'input_id': "first_vid", "video_name": "In Hearts Wake - Healer" }
    function videoInfo(jsonResp) {
        // var jsParsed = JSON.parse(JSON.stringify(jsonResp));
        var jsParsed = JSON.parse(jsonResp);

        // Which element is the input element
        var which_in = String(jsParsed['input_id']);
        document.getElementById(which_in).previousElementSibling.innerHTML = String(jsParsed['video_name']);
        document.getElementById(which_in).previousElementSibling.classList.toggle("hidden");

    }

    // JSONify input field that triggered this function
    function inJson(input_id, jVal) {
        var my_json = {'input_id': input_id, 'input_value': jVal};
        // Set up the XMLHttpRequest
        var my_http = new XMLHttpRequest();
        // Handle the server response
        my_http.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                videoInfo(this.responseText);
            }
            else if (this.readyState == 4 && this.status != 200) {
                var my_json = JSON.stringify({'input_id': input_id, 'video_name': "This URL threw an error.  Please double check it"})
                videoInfo(my_json);
            }
        };
        // POST my_json to server
        my_http.open("POST", "/checker");
        my_http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        my_http.send(JSON.stringify(my_json));

    }
    // Trigger inJson for onblur of each input field
    document.getElementById('first_vid').onblur = function(){
        if ((this.value).length > 2) {
            inJson(event.target.id, this.value);
        }
    };
    document.getElementById('second_vid').onblur = function(){
        if ((this.value).length > 2) {
            inJson(event.target.id, this.value);
        }    };
    document.getElementById('third_vid').onblur = function(){
        if ((this.value).length > 2) {
            inJson(event.target.id, this.value);
        }
    };
    document.getElementById('fourth_vid').onblur = function(){
        if ((this.value).length > 2) {
            inJson(event.target.id, this.value);
        }
    };
    document.getElementById('fifth_vid').onblur = function(){
        if ((this.value).length > 2) {
            inJson(event.target.id, this.value);
        }
    };





})();



