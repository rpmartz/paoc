(ns aoc.y15.day06
  (:require [aoc.utils :as u]
            [clojure.string :as str]))

(def lines (u/read-lines "y15/day06.txt"))

(defn parse-action
  "Determines whether a given line's instruction are to turn on, 
   turn off, or toggle the range"
  [line]
  (cond (str/starts-with? line "turn on") :on
        (str/starts-with? line "turn off") :off
        (str/starts-with? line "toggle") :toggle))

(defn enumerate-points [sx sy ex ey]
  (u/coordinate-square sx sy ex ey)
  )

(defn parse-line [line]
  (let [action (parse-action line)
        [sx sy ex ey] (mapv parse-long (u/ints line))]
    {:action action
     :points (u/coordinate-square sx sy ex ey)
    }))

(map parse-line lines)

(last (u/grid 1000 1000))

(count (enumerate-points 0 0 1000 0))
(u/coordinate-square 0 0 1000 0)
first

; 499,499 through 500,500
; should be four squares (499, 499), (499, 500)
(u/coordinate-square 499 499 (inc 500) (inc 500))
(u/coordinate-square 0 0 (inc 999) (inc 0))
