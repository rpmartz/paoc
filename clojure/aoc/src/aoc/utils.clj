(ns aoc.utils
  (:require [clojure.string :as str]))

(defn read-lines [filename]
  (str/split-lines (slurp (str "../../inputs/" filename))))

(defn read-input [filename]
  (slurp (str "../../inputs/" filename)))

(defn ints [s]
  (re-seq #"-?[0-9]+" s))

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



