(ns aoc.y21.day18-test
  (:require [clojure.test :refer :all]
            [aoc.y21.day18 :refer :all]))

(deftest test-split-fn
  (testing "Test splitting examples"
    (is (= [5 5] (split 10)))
    (is (= [5 6] (split 11)))
    (is (= [6 6] (split 12))))

  (testing "Throws exception if given list"
    (is (thrown? java.lang.AssertionError (split [4 4])))))

(deftest test-magnitude-fn
  (testing "Magnitude of a regular number"
    (is (= 4 (magnitude 4))))

  (testing "Magnitude of a list of two regular numbers"
    (is (= 29 (magnitude [9 1])))
    (is (= 21 (magnitude [1 9]))))

  (testing "Magnitude of a list of two lists"
    (is (= 129 (magnitude [[9 1] [1 9]]))))

  (testing "Magnitude of a list and a number"
    (is (= 89 (magnitude [[9 1] 1])))
    (is (= 45 (magnitude [1 [1 9]]))))

  (testing "Problem example calculations"
    (is (= 143 (magnitude  [[1 2] [[3 4] 5]])))
    (is (= 1384 (magnitude [[[[0 7] 4] [[7 8] [6 0]]] [8 1]])))
    (is (= 445 (magnitude [[[[1 1] [2 2]] [3 3]] [4 4]])))
    (is (= 791 (magnitude  [[[[3 0] [5 3]] [4 4]] [5 5]])))
    (is (= 1137 (magnitude  [[[[5 0] [7 4]] [5 5]] [6 6]])))
    (is (= 3488 (magnitude [[[[8 7] [7 7]] [[8 6] [7 7]]] [[[0 7] [6 6]] [8 7]]])))))