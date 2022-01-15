var form = $("#upload-form");
form.on('submit',function() {
　　var seed = Math.floor(Math.random() * 1000);
var id = "uploader-frame-" + seed;
var callback = "uploader-cb-" + seed;

var iframe = $('<iframe id="'+id+'" name="'+id+'" style="display:none;">');
var url = form.attr('action');
form.attr('target', id).append(iframe).attr('action', url + '?iframe=' + callback);
<script type="text/javascript">
　　window.top.window['callback'](data);
</script>
});
