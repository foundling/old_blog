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
