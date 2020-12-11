

var user = prompt('user id enter')
var pass = prompt('enter password')

var all_users; //storing all users fname id and last name

initChat(user, pass)

function initChat(user, pass){ 
  if(user!= null && user!= ""){
    EmpCode = user;
    $.ajax({
          url: '/login',
          type: 'POST',
          data: {
            userid: user,
            pass : pass
          },
          dataType: "json",
          success: function (response) {
            console.log(response);
            var time_id = Date.now();
            if(response!= null){
              $("#main").append(JSON.stringify(response));
              $("#main").append(
                '<button id="1" id2= '+response[0][3]+' onClick="reply_click(this.id, this.id2)">Add an Employee</button>'+
            '<button id="2" id2= '+response[0][3]+' onClick="reply_click(this.id, this.id2)">Delete an Employee</button>'+
            '<button id="3" id2= '+response[0][3]+' onClick="reply_click(this.id, this.id2)">Update an Employee</button>'
              )

            }
    
          
          else{
            console.log('not an hr')
          }
          }
        })
      }
      else{
        console.log('please give user id and pass')
      }
  }
  

  
function reply_click(clicked_id){
    if (clicked_id == 1){
      addEmployee(clicked_id)
    }
    else if (clicked_id == 2){
      DeleteEmp(clicked_id)
    }
    else{
      UpdateEmp(clicked_id)
    }
}


function addEmployee(clicked_id, hr_id){
  var emp_name = prompt('enter Emp name')
  var salary = prompt('enter Salary')
  $.ajax({
    url: '/addEmployee',
    type: 'POST',
    data: {
      emp_name: emp_name,
      salary : salary,
      hr_id: hr_id
    },
    dataType: "json",
    success: function (response) {
      console.log(response)
      if (response == 1){
      alert('EMployee Added Successfully')
      }
    }
  })
}

function DeleteEmp(clicked_id, hr_id){
  var emp_id = prompt('enter Emp id to Delete')
  $.ajax({
    url: '/DeleteEmployee',
    type: 'POST',
    data: {
      emp_id: emp_id,
      hr_id: hr_id
    },
    dataType: "json",
    success: function (response) {
      console.log(response)
      if (response == 1){
        alert('EMployee Deleted Successfully')
        }
    }
  })
}
function UpdateEmp(clicked_id, hr_id){
  var emp_id = prompt('WHich Employee you want to update? Enter EMp Number')
  var emp_name = prompt('enter New Name of Emp')
  var salary = prompt('enter New Salary')
  $.ajax({
    url: '/UpdateEmployee',
    type: 'PUT',
    data: {
      emp_id: emp_id,
      emp_name: emp_name,
      salary : salary,
      hr_id:hr_id
    },
    dataType: "json",
    success: function (response) {
      console.log(response)
      if (response == 1){
        alert('EMployee Updated Successfully')
        }
    }
  })
}
