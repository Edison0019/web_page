function now_y(){
    let now = new Date();
    let year = now.getFullYear();
    let output = 'Copyright &copy; ' + year  + ' · Edison Santana (Developer and Data Analyst)';
    return document.getElementById('time_year').innerHTML = output;
}