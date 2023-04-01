(ns aoc.utils
  (:require [clojure.string :as str]))

(defn read-lines [filename]
  (str/split-lines (slurp (str "../../inputs/" filename))))

(defn read-input [filename]
  (slurp (str "../../inputs/" filename)))

(defn coordinate-square
  "Returns a sequence of all points in the 2D square made by the points"
  [start-x start-y end-x end-y]
  (for [x (range start-x end-x)
        y (range start-y end-y)]
    [x y]))

(defn grid [numrows numcols]
  (for [x (range numrows)
        y (range numcols)
        ] [x y]))


(defn parse-ints [s]
  (re-seq #"-?[0-9]+" s))

(defn manhattan-distance
  "Calculates the Manhattan distance between two points.
   Expects points in [x y] format"
  [p1 p2]
  (let [x1 (first p1)
        y1 (second p1)
        x2 (first p2)
        y2 (second p2)]
    (+ (abs (- x1 x2)) (abs (- y1 y2)))))




