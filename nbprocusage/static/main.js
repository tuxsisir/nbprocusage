define([
    'jquery',
    'base/js/utils'
], function($, utils) {

    function setupDOM() {
        $('#maintoolbar-container').append(
            $('<div>').attr('id', 'mem-display')
            .addClass('btn-group')
            .addClass('pull-right')
            .append(
                $('<strong>').text('Mem: ')
            ).append(
                $('<span>').attr('id', 'usage-mem')
                .attr('title', 'Actively used memory (updates every 5s)')
            ),
            $('<div>').attr('id', 'cpu-display')
            .addClass('btn-group')
            .addClass('pull-right')
            .append(
                $('<strong>').text('CPU Usage: ')
            ).append(
                $('<span>').attr('id', 'usage-cpu')
                .attr('title', 'Actively used cpu (updates every 5s)')
            )
        );
    }
    function humanFileSize(size) {
        var i = Math.floor( Math.log(size) / Math.log(1024) );
        return ( size / Math.pow(1024, i) ).toFixed(1) * 1 + ' ' + ['B', 'kB', 'MB', 'GB', 'TB'][i];
    }
    var displayMetrics = function() {
        if (document.hidden) {
            return;
        }
        var kernel = IPython.notebook.kernel;
        $.ajax({
            url: utils.get_body_data('baseUrl') + 'resource',
            type: "GET",
            data: {
                kernel: kernel.id
            },
            dataType: 'json',
            success: function(data) {
                let cpuUsage = data['cpu'] + " %";
                let memUsage = humanFileSize(data['mem']) + " of " + humanFileSize(data['total_mem']);
                $('#usage-cpu').text(cpuUsage);
                $('#usage-mem').text(memUsage);
            }
        });
    };
    function load_ipython_extension() {
        setupDOM();
        displayMetrics();
        setInterval(displayMetrics, 1000 * 5);
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
