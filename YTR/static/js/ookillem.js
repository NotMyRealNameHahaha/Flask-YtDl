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

    // nav menu -> Mobile toggle
    document.getElementById("headerbtn").addEventListener("click", function() {
        kTog("headerdd", "active");
    });

    // Toggle function w/ event target
    function evtkTog(evt, evtKlass, which, what) {
        document.getElementById(which).classList.toggle(what);
        evt.currentTarget.classList.add(evtKlass);
    }


})();



