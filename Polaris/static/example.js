const quill = new Quill("#editor", {
    modules: {
        syntax: true,
        toolbar: "#toolbar-container",
    },
    placeholder: "Compose an epic...",
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
            url: "get_suggestion/" + text + "/",
            type: "GET",
            success: function(response){
                suggested_text = response.suggested_text;
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

        } else { console.log("Suggestion already inserted!") };

    });


    $("#submitBtn4ConfirmSuggestion").click(function () {

        if (suggesting) {

            const range = quill.getSelection();

            quill.deleteText(range.index, suggested_text.length);

            quill.insertText(range.index, suggested_text);

            suggesting = false;

        } else { console.log("Suggestion not inserted!") };

    });


    $("#submitBtn4DismissSuggestion").click(function () {

        if (suggesting) {

            const range = quill.getSelection();

            quill.deleteText(range.index, suggested_text.length);

            suggested_text = 'no available suggestion!';

            suggesting = false;

        } else { console.log("Suggestion not inserted!") };

    });


    $("#submitBtn").click(function () {

        const length = quill.getLength();
        const content = quill.getContents();
        const text = quill.getText(0, length);
        var jsonData = {
            length: length,
            content: content,
            text: text,
        };

        $.ajax({
            type: "POST",
            url: "process_json/",
            data: JSON.stringify(jsonData),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                alert("Data successfully sent!");
            },
            error: function (response) {
                alert("Error sending data!");
            },
        });
    });
});