window.onload = function(){
    document.getElementById('1').onclick = edit_student;
    function edit_student(){
        var student_name = document.getElementById('1').innerHTML;
        document.getElementById('edit_student').style.display = 'block';
        document.getElementById('student_name').setAttribute('value', student_name);
//        document.getElementById('1').innerHTML = document.getElementById('student_name').getAttribute('value');
    }
};
