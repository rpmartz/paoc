(ns aoc.y22.day15
  (:require [aoc.utils :as u]))

(def lines (u/read-lines "y22/day15.txt"))

(defn parse-coords
  "Takes each line of puzzle input and parses it to pair of [x, y] coordinates"
  [line]
  (let [[sensor-x sensor-y beacon-x beacon-y] (u/parse-ints line)]
    [(map parse-long [sensor-x sensor-y])
     (map parse-long [beacon-x beacon-y])]))

(defn calculate-m-dist [pair]
  (let [[[sx sy] [bx by]] pair]
    (+ (abs (- sx bx)) (abs (- sy by)))))

(def pairs
  (map parse-coords lines))

; map of  {:sensor (x y) :beacon (x y) :distance int}
(def measurements (reduce
                   (fn [acc pair]
                     (conj acc {:sensor (first pair)
                                :beacon (second pair)
                                :distance (calculate-m-dist pair)})) [] pairs))
