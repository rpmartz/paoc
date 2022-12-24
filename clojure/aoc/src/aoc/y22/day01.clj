(ns aoc.y22.day01
  (:require [clojure.string :as string]))

(def per-elf-str-values
  (string/split (slurp "../../inputs/y22/day01.txt") #"\n\n"))

(def per-elf-line-values
  (map #(string/split % #"\n") per-elf-str-values))

(def elf-calorie-values
  (loop [[line & lines] per-elf-line-values
         acc []]
    (if (empty? lines)
      acc
      (let [current-line-value (reduce + (map parse-long line))]
        (recur lines (conj acc current-line-value))))))

(defn part-1 []
  (apply max elf-calorie-values))

(defn part-2 []
  (reduce + (take 3 (reverse (sort elf-calorie-values)))))


(do
  (println (part-1))
  (println (part-2)))
