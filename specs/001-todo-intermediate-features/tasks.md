---

description: "Task list for Todo App – Intermediate Level Features implementation"
---

# Tasks: Todo App – Intermediate Level Features

**Input**: Design documents from `/specs/001-todo-intermediate-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification requires unit and integration tests for all new functionality.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 Initialize Python 3.13+ project with standard library dependencies only
- [X] T003 [P] Create __init__.py files in src/ and tests/ directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 [P] Update Task model in src/models.py with priority and tags fields
- [X] T005 [P] Update Task model validation rules to include priority and tags constraints
- [X] T006 [P] Update TaskOperations class in src/tasks.py to handle priority and tags
- [X] T007 [P] Update UI components in src/ui.py to support priority and tags input
- [X] T008 Create base test infrastructure in tests/ with unittest framework

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Assign Priorities & Tags (Priority: P1) 🎯 MVP

**Goal**: Enable users to assign priority levels (high, medium, low) and tags to tasks during creation and updates

**Independent Test**: Can be fully tested by adding a new task with priority and tags, and verifying they are correctly stored and displayed.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for Task model with priority and tags in tests/unit/test_models.py
- [X] T010 [P] [US1] Unit test for add_task with priority and tags in tests/unit/test_tasks.py
- [X] T011 [P] [US1] Unit test for update_task with priority and tags in tests/unit/test_tasks.py

### Implementation for User Story 1

- [X] T012 [US1] Implement Task model updates with priority and tags in src/models.py
- [X] T013 [US1] Implement add_task method updates to accept priority and tags in src/tasks.py
- [X] T014 [US1] Implement update_task method updates to modify priority and tags in src/tasks.py
- [X] T015 [US1] Update console UI to accept priority input during task creation in src/ui.py
- [X] T016 [US1] Update console UI to accept tags input during task creation in src/ui.py
- [X] T017 [US1] Update console UI to accept priority and tags during task updates in src/ui.py
- [X] T018 [US1] Update console UI to display priority and tags when viewing tasks in src/ui.py
- [X] T019 [US1] Add validation for priority values (high, medium, low) in src/tasks.py
- [X] T020 [US1] Add validation for tags format in src/tasks.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Search Tasks (Priority: P2)

**Goal**: Enable users to search tasks by keyword in the title or description

**Independent Test**: Can be fully tested by creating multiple tasks with different titles/descriptions and verifying search returns correct results.

### Tests for User Story 2 ⚠️

- [X] T021 [P] [US2] Unit test for search_tasks functionality in tests/unit/test_tasks_search.py
- [X] T022 [P] [US2] Test search with keyword in title in tests/unit/test_tasks_search.py
- [X] T023 [P] [US2] Test search with keyword in description in tests/unit/test_tasks_search.py

### Implementation for User Story 2

- [X] T024 [US2] Implement search_tasks method in src/tasks.py
- [X] T025 [US2] Add search functionality to UI menu in src/ui.py
- [X] T026 [US2] Implement search input handling in src/ui.py
- [X] T027 [US2] Add validation for search keyword input in src/tasks.py
- [X] T028 [US2] Handle edge case of empty search keyword in src/tasks.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Filter Tasks (Priority: P3)

**Goal**: Enable users to filter tasks by status (complete/incomplete), priority (high/medium/low), and tags

**Independent Test**: Can be fully tested by creating tasks with different statuses, priorities, and tags, then applying various filters.

### Tests for User Story 3 ⚠️

- [X] T029 [P] [US3] Unit test for filter_tasks by status in tests/unit/test_tasks_filter.py
- [X] T030 [P] [US3] Unit test for filter_tasks by priority in tests/unit/test_tasks_filter.py
- [X] T031 [P] [US3] Unit test for filter_tasks by tags in tests/unit/test_tasks_filter.py
- [X] T032 [P] [US3] Unit test for combined filter functionality in tests/unit/test_tasks_filter.py

### Implementation for User Story 3

- [X] T033 [US3] Implement filter_tasks method in src/tasks.py
- [X] T034 [US3] Add filter functionality to UI menu in src/ui.py
- [X] T035 [US3] Implement filter criteria input handling in src/ui.py
- [X] T036 [US3] Implement combined filtering logic in src/tasks.py
- [X] T037 [US3] Add validation for filter criteria in src/tasks.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Sort Tasks (Priority: P4)

**Goal**: Enable users to sort tasks by priority (high → low), title (alphabetically), or due date

**Independent Test**: Can be fully tested by creating tasks with different priorities/dates/titles and verifying they appear in the correct order after sorting.

### Tests for User Story 4 ⚠️

- [X] T038 [P] [US4] Unit test for sort_tasks by priority in tests/unit/test_tasks_sort.py
- [X] T039 [P] [US4] Unit test for sort_tasks by title in tests/unit/test_tasks_sort.py
- [X] T040 [P] [US4] Unit test for sort_tasks by due date in tests/unit/test_tasks_sort.py

### Implementation for User Story 4

- [X] T041 [US4] Implement sort_tasks method in src/tasks.py
- [X] T042 [US4] Add sort functionality to UI menu in src/ui.py
- [X] T043 [US4] Implement sort criteria input handling in src/ui.py
- [X] T044 [US4] Implement priority sorting logic (high → low) in src/tasks.py
- [X] T045 [US4] Implement title sorting logic (alphabetically) in src/tasks.py
- [X] T046 [US4] Implement due date sorting logic in src/tasks.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T047 [P] Update main.py to integrate all new features with UI
- [X] T048 [P] Add comprehensive error handling for all new features in src/tasks.py
- [X] T049 [P] Add docstrings to all new methods and functions
- [X] T050 [P] Create integration tests for combined functionality in tests/integration/test_main.py
- [ ] T051 [P] Performance testing to ensure operations complete in under 1 second for up to 1000 tasks
- [X] T052 [P] Update README.md with new features documentation
- [ ] T053 Run quickstart.md validation to ensure all features work as described

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for Task model with priority and tags in tests/unit/test_models.py"
Task: "Unit test for add_task with priority and tags in tests/unit/test_tasks.py"
Task: "Unit test for update_task with priority and tags in tests/unit/test_tasks.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Implement Task model updates with priority and tags in src/models.py"
Task: "Implement add_task method updates to accept priority and tags in src/tasks.py"
Task: "Implement update_task method updates to modify priority and tags in src/tasks.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence