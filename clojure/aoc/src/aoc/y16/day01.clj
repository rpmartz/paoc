(ns aoc.y16.day01
  (:require [aoc.utils :as u]
            [clojure.string :as s]
            [clojure.core.match :refer [match]]))

(def input (u/read-input "y16/day01.txt"))

(defn parse-direction [instruction]
  (keyword (str (first instruction))))

(defn parse-distance [instruction]
  (parse-long (str (s/join (rest instruction)))))

(defn get-new-dir [currently-facing turn-direction]
  (match [currently-facing turn-direction]
    [:north :R] :east
    [:north :L] :west
    [:east :R] :south
    [:east :L] :north
    [:south :L] :east
    [:south :R] :west
    [:west :R] :north
    [:west :L] :south))

(defn move
  "Executes an instruction and returns an updated location based on what the instruction would do"
  [state instruction]
  ;; determine 
  (let [curdir (get state :facing)
        curloc (get state :location)
        turndir (parse-direction instruction)
        magnitude (parse-distance instruction)
        newdir (get-new-dir curdir turndir)]

    (cond
      (= newdir :north) {:facing newdir :location [(first curloc) (+ magnitude (second curloc))]}
      (= newdir :east) {:facing newdir :location [(+ magnitude (first curloc)) (second curloc)]}
      (= newdir :south) {:facing newdir :location [(first curloc) (- magnitude (second curloc))]}
      (= newdir :west)  {:facing newdir :location [(+ magnitude (first curloc)) (second curloc)]})))

(defn follow-instructions [] 
  (let [initial-state {:location [0 0] :facing :north}
        instructions (s/split input #", ")]
    (reduce (fn [state instruction] (move state instruction)) initial-state instructions))
  )

(defn part-1 []
  )

(u/manhattan-distance [0 0] (get ( follow-instructions) :location))


(follow-instructions)
(parse-direction "L54")
(parse-distance "L566")
(rest "L56")