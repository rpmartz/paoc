(ns aoc.y21.day18
  (:require [aoc.utils :as u]))

; sfish-reduce
(defn sfish-reduce [num]
  (println "Implement me"))

(defn explode [num])

(defn sfish-add [l r]
  [l r]
  )

(defn split
  "To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on."
  [num]
  (assert (number? num))
  [(int (Math/floor (/ num 2)))
   (int (Math/ceil (/ num 2)))])

(defn magnitude
  "The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number."
  [snailfish-num]
  (cond
    (number? snailfish-num) snailfish-num
    :else (+ 
           (* 3 (magnitude (first snailfish-num))) 
           (* 2 (magnitude (second snailfish-num))))))