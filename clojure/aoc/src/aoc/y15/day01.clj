(ns aoc.y15.day01
  (:require [aoc.utils :as u]))

(def input (u/read-input "y15/day01.txt"))

(defn paren-reducer [acc x]
  (if (= \( x)
    (inc acc)
    (dec acc)))

(defn part-1 []
  (let [ans (reduce paren-reducer 0 input)]
    (println (str "Part 1: " ans))))

(defn part-2 []
  (let [ans (->> (reductions paren-reducer 0 input)
                 (map-indexed vector)
                 (drop-while #(>= (second %) 0))
                 (ffirst))]
    (println (str "Part 2: " ans))))

(do
  (part-1)
  (part-2))



