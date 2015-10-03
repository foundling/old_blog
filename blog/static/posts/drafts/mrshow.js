/*var Corporation = function() {

  this.employees = {
    employee1: {
      name:'Store Clerk',
      boss: this.employees.employee2,
      execPower: false,
    },
    employee2: {
      name:'Store Manager',
      boss: this.employees.employee3,
      execPower: false,
    },
    employee3: {
      name:'Regional Manager',
      boss: this.employees.employee4,
      execPower: false,
    },
    employee4: {
      name: 'Corporate Executive',
      boss: this.employees.employee5,
      execPower: false,
    },
    employee5: {
      name: 'President of the United States',
      boss: null,
      execPower: true,
      changeForADollarPossible: function() {
        return 'no';
      }
    }
 };
};
*/


var getAnswer = function(employee) {
  if (employee.changeForADollarPossible) return employee.changeForADollarPossible(); 
  else return getAnswer(employee.boss);
};

console.log(new Corporation());
