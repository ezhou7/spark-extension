/*
 * Copyright 2022 G-Research
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package uk.co.gresearch.spark.diff.comparator

import org.apache.spark.sql.Column
import org.apache.spark.sql.functions.{abs, greatest}

case class EpsilonDiffComparator(epsilon: Double, relative: Boolean = true, inclusive: Boolean = true)
  extends DiffComparator {
  override def equiv(left: Column, right: Column): Column = {
    val threshold = if (relative)
      greatest(abs(left), abs(right)) * epsilon
    else
      epsilon

    val inEpsilon = if (inclusive)
      (diff: Column) => diff <= threshold
    else
      (diff: Column) => diff < threshold

    left.isNull && right.isNull || left.isNotNull && right.isNotNull && inEpsilon(abs(left - right))
  }

  def asAbsolute(): EpsilonDiffComparator = if (relative) copy(relative = false) else this
  def asRelative(): EpsilonDiffComparator = if (relative) this else copy(relative = true)

  def asInclusive(): EpsilonDiffComparator = if (inclusive) this else copy(inclusive = true)
  def asExclusive(): EpsilonDiffComparator = if (inclusive) copy(inclusive = false) else this
}
