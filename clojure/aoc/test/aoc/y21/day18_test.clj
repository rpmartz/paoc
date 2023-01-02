(ns aoc.y21.day18-test
  (:require [clojure.test :refer :all]
            [aoc.y21.day18 :refer :all]))

(deftest test-split-fn
  (testing "Test splitting examples"
    (is (= [5 5] (split 10)))
    (is (= [5 6] (split 11)))
    (is (= [6 6] (split 12))))
  
  (testing "Throws exception if given list"
    (is (thrown? java.lang.AssertionError (split [4 4])))
    )
  )