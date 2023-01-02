(ns aoc.y21.day18
  (:require [aoc.utils :as u]))

; sfish-reduce
(defn sfish-reduce [num]
  (println "Implement me"))

(defn explode [num])

(defn split
  "To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on."
  [num]
  [(int (Math/floor (/ num 2)))
   (int (Math/ceil (/ num 2)))])