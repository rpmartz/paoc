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

(defn parse-line [line]
  (let [action (parse-action line)
        [sx sy ex ey] (u/ints line)]
    {:action action
     :start (mapv parse-long [sx sy])
     :end (mapv parse-long [ex ey])}))

(map parse-line lines)
