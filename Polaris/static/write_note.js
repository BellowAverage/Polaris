$("#editor").css("border", "none")
// $("#editor").css("border-left", "5px solid black");
$("#toolbar-container").css("display", "flex")
$("#toolbar-container").css("flex-direction", "row")
$("#toolbar-container").css("gap", "0.1rem")


const quill = new Quill("#editor", {
    modules: {
        syntax: true,
        toolbar: "#toolbar-container",
    },
    placeholder: "· Start your note here ...",
    theme: "snow",
});

$(document).ready(function () {

    var suggested_text = 'Suggesting Text';

    var suggesting = false;

    $("#submitBtn4RequestSuggestion").click(function () {

        const length = quill.getLength();
        // const content = quill.getContents();
        const text = quill.getText(0, length);

        $.ajax({
            url: "/app01/function/get_suggestion/" + text + "/",
            type: "GET",
            success: function(response){
                suggested_text = response.suggested_text;
                $("#response_section").prepend(`<p class="plain_text" style="color:red;">· Get "${suggested_text}" as suggested text.</p>`)
            },
            error: function(xhr, errmsg, err){
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });


    $("#submitBtn4InsertSuggestion").click(function () {

        if (!suggesting) {

            const range = quill.getSelection();

            quill.insertText(range.index, suggested_text, {
                color: '#808080',
                italic: true,
            });

            quill.setSelection(range.index);

            suggesting = true;

            $("#response_section").prepend(`<p class="plain_text" style="color:red;">· Suggested text inserted.</p>`)

        } else { console.log("Suggestion already inserted!") };

    });


    $("#submitBtn4ConfirmSuggestion").click(function () {

        if (suggesting) {

            const range = quill.getSelection();

            quill.deleteText(range.index, suggested_text.length);

            quill.insertText(range.index, suggested_text);

            suggesting = false;

            $("#response_section").prepend(`<p class="plain_text" style="color:red;">· Suggested text confirmed.</p>`)

        } else { console.log("Suggestion not inserted!") };

    });


    $("#submitBtn4DismissSuggestion").click(function () {

        if (suggesting) {

            const range = quill.getSelection();

            quill.deleteText(range.index, suggested_text.length);

            suggested_text = 'no available suggestion!';

            suggesting = false;

            $("#response_section").prepend(`<p class="plain_text" style="color:red;">· Suggested text discarded.</p>`)

        } else { console.log("Suggestion not inserted!") };

    });


    // $("#submitBtn").click(function () {

    //     const length = quill.getLength();
    //     const content = quill.getContents();
    //     const text = quill.getText(0, length);
    //     var jsonData = {
    //         length: length,
    //         content: content,
    //         text: text,
    //     };

    //     $.ajax({
    //         type: "POST",
    //         url: "process_json/",
    //         data: JSON.stringify(jsonData),
    //         contentType: "application/json; charset=utf-8",
    //         dataType: "json",
    //         success: function (response) {
    //             alert("Data successfully sent!");
    //         },
    //         error: function (response) {
    //             alert("Error sending data!");
    //         },
    //     });
    // });
});