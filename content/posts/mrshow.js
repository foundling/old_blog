var employee5 = {
  name: 'President of the United States',
  boss: null,
  authorize: function() {
    return 'no';
  }
};
var employee4 = {
  name: 'Corporate Executive',
  boss: employee5,
};
var employee3 = {
  name:'Regional Manager',
  boss: employee4,
};
var employee2 = {
  name:'Store Manager',
  boss: employee3,
};
var employee1 = {
  name:'Store Clerk',
  boss: employee2,
};
var customer = {
  name: 'A. Guy',
  say: function(phrase) { console.log(phrase)},
  getChangeForADollar: function(employee) {
    console.log('Asking the %s ...', employee.name);
    if (employee.authorize) {
      var answer = employee.authorize();
      return 'the answer is ' + answer +'.'; 
    }
    else {
      return customer.getChangeForADollar(employee.boss);
    }
  }
};

customer.say('Could I have change for a dollar?');
console.log(customer.getChangeForADollar(employee1));
