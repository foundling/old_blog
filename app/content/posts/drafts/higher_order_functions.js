const moment = require('moment');
const assert = require('assert');
const users = [ 'alice', 'bob', 'fred' ];
const filenames = [ 

    'alice_2016-12-07.json',
    'alice_2016-12-04.json',
    'alice_2016-12-09.json',
    'alice_2016-12-01.json',
    'alice_2016-12-03.json',
    'alice_2016-12-11.json',
    'alice_2016-12-31.json',
    'bob_2016-12-03.json',
    'bob_2016-12-09.json',
    'bob_2016-12-02.json'

];



const dateComparator = (descending) => (a,b) => {
    return descending ? 
        moment(b).unix() - moment(a).unix():
        moment(a).unix() - moment(b).unix();
};

const range = (max) => [ ...Array(max).keys() ];
assert(range(5).length === 5);

const parseDateString = (filename) => filename.split('_')[1].split('.')[0];
assert(parseDateString('test_2016-12-01.json') === '2016-12-01'); 

const generateDateRange = (start, stop) => {

    let [ startDate, stopDate ] = [ moment(start), moment(stop) ];
    let diff = moment.duration(stopDate.diff(startDate)).days();

    return range(diff + 1).map(offset => startDate.clone().add({ days: offset }).format('YYYY-MM-DD'));
    
};

assert(generateDateRange('2016-12-01','2016-12-05').length === 5);
assert(generateDateRange('2016-12-01','2016-12-05').includes('2016-12-01'));
assert(generateDateRange('2016-12-01','2016-12-05').includes('2016-12-02'));
assert(generateDateRange('2016-12-01','2016-12-05').includes('2016-12-03'));
assert(generateDateRange('2016-12-01','2016-12-05').includes('2016-12-04'));
assert(generateDateRange('2016-12-01','2016-12-05').includes('2016-12-05'));

const belongsTo = (user) => (filename) => filename.split('_')[0] === user;
assert(belongsTo('test')('test_2016-12-01.json'));
const inDateRange = (start, stop) => (dateString) => moment(dateString).isBetween(moment(start), moment(stop), null, '[]');

const getMissingDates = (user, filenames, { start, stop }) => {

    const idealDates = generateDateRange(start, stop);

    const userFilesInRange = filenames
        .filter( belongsTo(user) )
        .filter( filename => inDateRange(start, stop)(parseDateString(filename)) );

    return idealDates
        .filter(idealDate => !userFilesInRange.map(parseDateString).includes(idealDate));

};

const missingDataReport = (users, filenames, dateRange) => {

    const reportSchema = {
        dateRange: null,
        users: {}
    };

    console.log();

    const run = () => { 

        let data = users.reduce((obj, user) => {

            obj['dateRange'] = dateRange; 
            obj['users'][user] = { 
                'missingDates': getMissingDates(user, filenames, dateRange),
                'files': filenames.filter(belongsTo(user))
            };

            return obj;

        }, reportSchema);

        return data;

    };

    return { run };

};

const data = missingDataReport(users, filenames, { start: '2016-12-01', stop: '2016-12-15' }).run();
console.log(JSON.stringify(data, null, 2));
