function play(position) {
    fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'position=' + position,
    })
    .then(response => response.text())
    .then(result => {
        if (result) {
            if (result.substring(result.length - 5) == 'wins!') {
                alert(result);
            }
//            alert(result);
            window.location.href = '/';
        } else {
            window.location.reload();
        }
    });
}

function reset() {
    fetch('/reset')
    .then(() => {
        window.location.href = '/';
    });
}
