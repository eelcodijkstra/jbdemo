function patch_thebe_config () {
    const scriptlist = $('script[type="text/x-thebe-config"]');
    if (scriptlist.length > 0) {
        const script = scriptlist[0];
        script.innerHTML = script.innerHTML.replace('kernelName', 'name');
    }
}

$(document).ready(patch_thebe_config);