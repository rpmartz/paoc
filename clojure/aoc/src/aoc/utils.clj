(ns aoc.utils
  (:require [clojure.string :as str]))

(defn read-lines [filename]
  (str/split-lines (slurp (str "../../inputs/" filename)))
  )

(defn read-input [filename]
  (slurp (str "../../inputs/" filename))
  )

(defn parse-ints [s]
  (re-seq #"-?[0-9]+" s))



