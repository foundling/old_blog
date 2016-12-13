var customer = {
  name: 'customer',
  say: function(phrase) { console.log(phrase)},
  getChangeForADollar: function(employee) {
    if (employee.authorize) {
      var answer = employee.authorize();
      return 'the answer is ' + answer +'.'; 
    }
    else {
      return this.getChangeForADollar(employee.boss);
    }
  }
};
