#!/usr/bin/node
exports.logMe = function (item) {
  return FileList.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
