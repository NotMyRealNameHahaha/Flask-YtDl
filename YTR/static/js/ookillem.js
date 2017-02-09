(function() {
    // Easy toggle function
    function kTog(which, what) {
        document.getElementById(which).classList.toggle(what);
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
        // document.getElementById("get_music").innerHTML = "Get songs";
    };

    /**  URL validator function for Download & Checking methods  */
    function urlErr(inpId, errMsg) {
        document.getElementById(inpId).previousElementSibling.innerHTML = errMsg;
        document.getElementById(inpId).previousElementSibling.classList.remove("hidden");
    }

/**
 *     Download methods
 *=============================================================== */

    document.getElementById("dlform").addEventListener("submit", function(evt){
        evt.preventDefault();
        console.log(this);
        /**
         * 1. Iterate over the text input fields
         * 2. POST input.value[i] to this.getAttribute('action');
         * 3. Use the responseText to handle errors/success
         */

        // What URL you're posting it to
        const purl = String(this.action);
        console.log(purl);


        let inField = this.querySelectorAll("input[type=text]");
        for (let i = 0; i < inField.length; i++) {
            // Make sure it's a URL
            if (inField[i].value.length >= 10 &&
                inField[i].value.includes("https://www.youtube.com/watch?")) {
                console.log(inField[i].id, inField[i].value);
                submitter(inField[i].id, inField[i].value);

            }
            // Handle non-Youtube URLs
            else if ( inField[i].value.length > 0 &&
                !inField[i].value.includes("https://www.youtube.com/watch?")) {
                let emsg = "This URL threw an error.  Please double check it";
                urlErr(inField[i].id, emsg);
            }
        }



        function submitter(inpId, inpVal) {
            let xm = new XMLHttpRequest();
            // POST data
            let my_json = {'input_id': inpId, 'input_value': inpVal};
            xm.open("POST", purl);
            xm.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xm.send(JSON.stringify(my_json));
            xm.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    console.log(this.responseText);
                }
            };
        }

    });




/**
 *
 *
 *
 *   v-------v          URL Checking methods         v-----------v
 *
 * ======================================================================*
 * ======================================================================*
 * ======================================================================*
 * ======================================================================*
 * ======================================================================*
 * ======================================================================*/

    /**  Input Field Event Listeners */
    document.getElementById("dlform").addEventListener("click", function(evt) {
        /**
         *  This method coincides with function testUrl()
         *  & facilitates URL checking
         * ============================================= */
        // Check if evt.target == TEXT input field
        if ( (evt.target && evt.target.nodeName == "INPUT")
             && (evt.target.getAttribute("type") == "text") )
        {
            evt.target.onblur = function() {
                if (this.value.length >= 10) {
                    // Send this element's id + its value to testUrl
                    let iid = this.id;
                    let iv = this.value;
                    // Send it to the checker URL
                    let curl = "/checker";
                    testUrl(iid, iv, curl);
                    // Log it for your sanity
                    console.log(iid);
                }
                else { }
            }
        }
    });

    function testUrl(inid, inVal, inUrl) {
        /**
         *  TEST the URL.  Valid URLs return the video title
         *                 Invalid URLs get this response:
         *                              {
         *                                "input_id": input_id,
         *                                "error": "Double check that URL."
         *                              }
         * @param {string} inid == id of an input field
         * @param {string} inVal == value of an input field (Youtube URL)
         */
        let my_json = {'input_id': inid, 'input_value': inVal};
        // Set up the XMLHttpRequest
        let my_http = new XMLHttpRequest();
        // Handle the server response
        my_http.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                urlConfirmer(this.responseText);
            }
            else if (this.readyState == 4 && this.status != 200) {
                let my_json = JSON.stringify({'input_id': inid, 'video_name': "This URL threw an error.  Please double check it"});
                urlConfirmer(my_json);
            }
        };
        // POST my_json to server
        my_http.open("POST", inUrl);
        my_http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        my_http.send(JSON.stringify(my_json));
    }




    function urlConfirmer(vResp) {
        let ihtml;

        let jsParsd = JSON.parse(vResp);
        let which_in = String(jsParsd['input_id']);
        if (jsParsd["error"]) {
            ihtml = String(jsParsd['error']);
            urlErr(which_in, ihtml);
        }
        else {
            ihtml = String(jsParsd['video_name']);
            document.getElementById(which_in).previousElementSibling.innerHTML = ihtml;
            document.getElementById(which_in).previousElementSibling.classList.remove("hidden");
        }
    }




    // TODO:  Add methods for handling server response (ie. the shell output)
/**
 *      v-------v       Old Methods     v-------------v
 *=============================================================== */
    //
    //
    // // Input checker
    // document.querySelector("#get_music").onclick = function() {
    //     let ins = document.querySelectorAll("input[type=text]");
    //
    //     for (let i=0; i < ins.length; i++) {
    //         if (ins[i].value.length > 15) {
    //             inJson(ins[i].id, ins[i].value);
    //         }
    //     }
    //
    // };
    //
    //
    // // Trigger inJson for onblur of each input field
    // document.getElementById('first_vid').onblur = function(){
    //     if ((this.value).length > 15) {
    //         inJson(event.target.id, this.value);
    //     }
    // };
    // document.getElementById('second_vid').onblur = function(){
    //     if ((this.value).length > 15) {
    //         inJson(event.target.id, this.value);
    //     }    };
    // document.getElementById('third_vid').onblur = function(){
    //     if ((this.value).length > 15) {
    //         inJson(event.target.id, this.value);
    //     }
    // };
    // document.getElementById('fourth_vid').onblur = function(){
    //     if ((this.value).length > 15) {
    //         inJson(event.target.id, this.value);
    //     }
    // };
    // document.getElementById('fifth_vid').onblur = function(){
    //     if ((this.value).length > 15) {
    //         inJson(event.target.id, this.value);
    //     }
    // };
    //
    //
    //
    //


})();



