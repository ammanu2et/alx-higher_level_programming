#!/usr/bin/node
exports.esrever = function (list) {
  return FileList.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
