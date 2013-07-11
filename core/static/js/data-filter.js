/**
 * Created with PyCharm.
 * User: Mario
 * Date: 10/07/13
 * Time: 08:12
 * To change this template use File | Settings | File Templates.
 */
(function ($) {
    // custom css expression for a case-insensitive contains()
    /**
     * @return {boolean}
     */
    jQuery.expr[':'].Contains = function (a, i, m) {
        return (a.textContent || a.innerText || "").toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };


    function listFilter(header, list) { // header is any element, list is an unordered list
        // create and add the filter form to the header
        var form = $("<form>").attr({
                "class": "filterform",
                "action": ".",
                "method": "get"}
            ),
            input = $("<input>").attr({
                "class": "filterinput",
                "type": "text",
                "placeholder": "Pesquisa por código",
                "name": "quadro"
            });
        $(form).append(input).appendTo(header);

        $(input)
            .change(function () {
                var filter = $(this).val();
                if (filter) {
                    // this finds all links in a list that contain the input,
                    // and hide the ones not containing the input while showing the ones that do
                    $(list).find("li[data-filter]:not(:Contains(" + filter + "))").hide();
                    $(list).find("li[data-filter]:Contains(" + filter + ")").show();
                } else {
                    $(list).find("li").show();
                }
                return false;
            })
            .keyup(function () {
                // fire the above change event after every letter
                $(this).change();
            });
    }

    //ondomready
    $(function () {
        listFilter($(".data-filter"), $(".thumbnails"));
    });
}(jQuery));