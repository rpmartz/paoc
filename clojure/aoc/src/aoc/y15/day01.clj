(ns aoc.y15.day01
  (:require [clojure.string :as str]
            [aoc.utils :as u]))

(def input (u/read-input "y15/day01.txt"))

(defn paren-reducer [acc x]
  (if (= \( x)
    (inc acc)
    (dec acc)))

(defn part-1 []
  (let [ans (reduce paren-reducer 0 input)]
    (println (str "Part 1: " ans))))

(do
  (part-1))