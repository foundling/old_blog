const moment = require('moment');
const filenames = [

    '2016-12-01.json',
    '2016-08-10.txt',
    '2016-12-12.json',
    '2015-12-01.txt',
    '2015-12-25.json',
    '2016-09-01.json',
    '2015-12-25.json',

];

const endsWith = ( suffix ) => filename.endsWith(suffix); 
const inDateRange = ( start, end ) => {
    return (date) => {
        return moment(date).isBetween( moment(start), moment(end));
    }
};


/* 
    Get files in a given date range.  
 */

filenames
    .filter(endsWith('.json'))
    .filter(inDateRange())
