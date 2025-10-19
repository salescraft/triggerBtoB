# 🧪 Testing Guide - Ultimate Intent Guide

## 🔗 Live URL
**https://8000-ikyyo3im55ycrlf2hqx1g-cbeee0f9.sandbox.novita.ai**

---

## ✅ Feature Testing Checklist

### 1. ⚡ Live Signal Feed (Top Section)
**Location:** First section after hero

**Tests:**
- [ ] Wait 8 seconds → New signal should slide in at the top
- [ ] Check animated pulse dots → Should be pulsing
- [ ] Verify time labels → Show "X min ago" / "X hours ago"
- [ ] Color coding → Blue (tech), Green (person), Purple (product), Orange (company)
- [ ] Feed length → Max 6 signals displayed at once

**Expected Behavior:**
- Auto-updates every 8 seconds
- Smooth slide-in animation
- Oldest signals disappear when feed exceeds 6 items

---

### 2. 📊 ROI Calculator
**Location:** Section after Live Feed (#calculator)

**Tests:**
1. **Monthly Prospects Slider:**
   - [ ] Move slider → Value updates instantly
   - [ ] Range: 100 to 5,000
   - [ ] Display updates: "X" format (e.g., "500")

2. **Reply Rate Slider:**
   - [ ] Move slider → Value updates with "%"
   - [ ] Range: 1% to 20%
   - [ ] Display: "X.X%" format (e.g., "5.5%")

3. **Meeting Rate Slider:**
   - [ ] Range: 10% to 60%
   - [ ] Display: "X%" format (e.g., "30%")

4. **Deal Size Slider:**
   - [ ] Range: $1,000 to $100,000
   - [ ] Display: "$X,XXX" format with commas (e.g., "$10,000")

5. **Close Rate Slider:**
   - [ ] Range: 5% to 50%
   - [ ] Display: "X%" format (e.g., "20%")

**Results Panel Tests:**
- [ ] Current Pipeline → Updates instantly
- [ ] Signal Pipeline → Shows higher value (+200% boost)
- [ ] Monthly Increase → Shows green difference
- [ ] Annual Impact → 12x monthly increase
- [ ] Time Saved → Calculates hours saved

**CTA Test:**
- [ ] Click "Unlock This ROI" → Opens lemlist Intent page in new tab
- [ ] Check UTM params: `utm_medium=roi_calculator`

**Expected Math:**
```
Example: 500 prospects, 5% reply, 30% meeting, $10K deal, 20% close
Current: 500 × 0.05 × 0.30 × 0.20 × $10K = $15,000/month
With Signals: 500 × 0.10 × 0.45 × 0.20 × $10K = $45,000/month
Increase: $30,000/month → $360,000/year
```

---

### 3. 🎯 Signal Prioritization Matrix
**Location:** After ROI Calculator (#matrix)

**Visual Tests:**
- [ ] Matrix displays with gradient background (green → yellow → red)
- [ ] Grid lines visible
- [ ] 12 colored dots positioned correctly:
  - Green = High strength (🔥🔥🔥)
  - Orange = Medium strength (🔥🔥)
  - Blue = Low strength (🔥)

**Interaction Tests:**
1. **Hover Over Dots:**
   - [ ] Dot scales up (1.5x size)
   - [ ] Info panel appears below matrix
   - [ ] Info shows: Name, Strength (🔥), Description, Detection Ease, Best For

2. **Test Each Quadrant:**
   - [ ] Top-Left (Quick Wins) → Has green "Champion Job Change", etc.
   - [ ] Top-Right (High Value) → Has orange/green dots
   - [ ] Bottom-Left (Low Hanging) → Has blue dots
   - [ ] Bottom-Right (Avoid) → Has red area (ideally no dots)

**Sample Signals to Test:**
- "Champion Job Change" → Top-left, green, 🔥🔥🔥
- "Funding Round" → Mid-left, orange, 🔥🔥
- "Event Attendance" → Bottom-center, blue, 🔥

**Usage Guide:**
- [ ] Yellow box below matrix explains quadrants
- [ ] Clear instructions for each quadrant type

---

### 4. 🎯 Signal IQ Quiz
**Location:** After Signal Matrix (#quiz)

**Setup:**
- [ ] Purple gradient background
- [ ] "7 questions" badge visible
- [ ] First question loads automatically

**Question Flow:**
1. **Question 1:** Series B funding scenario
   - [ ] 4 answer options visible
   - [ ] Click an answer → Advances to Q2
   - [ ] Progress bar updates (14% → 28%)

2. **Question 2-6:** Continue clicking answers
   - [ ] Progress bar advances each time
   - [ ] Score counter updates (top-right)
   - [ ] Smooth transitions

3. **Question 7:** Final question
   - [ ] Click answer → Quiz disappears
   - [ ] Results screen appears

**Results Screen:**
- [ ] Score displayed: "X / 70" format
- [ ] Level badge shows (🏆/⭐/📈/🌱)
- [ ] Personalized feedback message
- [ ] CTA button: "Level Up with lemlist Intent"
- [ ] Click CTA → Opens lemlist page with `utm_medium=quiz`

**Scoring Logic:**
- 80%+ (56-70 pts) = 🏆 Signal Master
- 60-79% (42-55 pts) = ⭐ Signal Pro
- 40-59% (28-41 pts) = 📈 Signal Student
- <40% (0-27 pts) = 🌱 Signal Novice

**Edge Cases:**
- [ ] All correct answers → 70/70 points
- [ ] All wrong answers → 0/70 points

---

### 5. 📥 Downloadable Resources
**Location:** After Quiz (#resources)

**6 Resource Cards:**
1. **📕 PDF Guide (Red)**
   - [ ] Icon displays
   - [ ] "Download PDF" button
   - [ ] Click → Alert prompts email entry

2. **📊 Spreadsheet (Green)**
   - [ ] "Get Spreadsheet" button
   - [ ] Click → Alert prompts email entry

3. **📝 Notion (Purple)**
   - [ ] "Duplicate Template" button
   - [ ] Click → Alert prompts email entry

4. **✉️ Email Templates (Blue)**
   - [ ] "Get Templates" button
   - [ ] Click → Alert prompts email entry

5. **⚙️ Automation (Yellow)**
   - [ ] "Get Scripts" button
   - [ ] Click → Alert prompts email entry

6. **✅ Checklist (Indigo)**
   - [ ] "Get Checklist" button
   - [ ] Click → Alert prompts email entry

**Email Capture Form:**
- [ ] Email input field functional
- [ ] "Send Me Everything" button
- [ ] Enter email → Click submit
- [ ] Success alert appears
- [ ] After 2 seconds → Redirects to lemlist trial
- [ ] Check UTM: `utm_medium=resources`

**Visual Tests:**
- [ ] 3-column grid on desktop
- [ ] 1-column stack on mobile
- [ ] Hover effects on cards
- [ ] Gradient backgrounds unique per card

---

### 6. 📚 Glossary
**Location:** After Resources (#glossary)

**Layout:**
- [ ] 2-column grid on desktop
- [ ] 12 term cards visible

**Term Cards:**
1. **Buying Signal** (first card)
   - [ ] Blue header "Buying Signal"
   - [ ] Definition paragraph
   - [ ] Hover → Slight highlight effect

2. **Intent Data**
   - [ ] Clear definition
   - [ ] Hover effect

3. **Continue for all 12 terms**
   - [ ] PQL, MQL, Trigger Event, etc.
   - [ ] All cards styled consistently

**Further Reading:**
- [ ] Blue box at bottom
- [ ] 4 linked resources
- [ ] Links have hover effects (blue color)

**Hover Behavior:**
- [ ] Card background changes to light blue
- [ ] Slight left padding increase
- [ ] Smooth transition

---

## 🎨 Cross-Browser Testing

### Desktop Browsers:
- [ ] **Chrome** → All features work
- [ ] **Firefox** → All features work
- [ ] **Safari** → All features work
- [ ] **Edge** → All features work

### Mobile Testing:
- [ ] **iOS Safari** → Responsive layout
- [ ] **Android Chrome** → Responsive layout
- [ ] Touch interactions work (no hover-only features)
- [ ] All sliders draggable on touch screens

---

## 📱 Responsive Breakpoints

### Mobile (< 768px):
- [ ] Hero text scales down
- [ ] CTAs stack vertically
- [ ] Signal Matrix adjusts
- [ ] Quiz cards full-width
- [ ] Resource grid becomes 1-column
- [ ] Glossary becomes 1-column

### Tablet (768px - 1024px):
- [ ] Resource grid becomes 2-column
- [ ] Glossary stays 2-column
- [ ] Matrix maintains aspect ratio

### Desktop (> 1024px):
- [ ] Resource grid becomes 3-column
- [ ] All features optimal layout
- [ ] Max-width containers (5xl, 6xl)

---

## 🚀 Performance Tests

### Load Time:
- [ ] Page loads in < 3 seconds
- [ ] No render-blocking resources
- [ ] Smooth animations (60fps)

### JavaScript:
- [ ] No console errors
- [ ] Calculator updates instantly (<100ms)
- [ ] Quiz transitions smooth
- [ ] Live feed updates on time (8s intervals)

### Accessibility:
- [ ] All CTAs keyboard accessible (Tab navigation)
- [ ] Focus states visible
- [ ] Color contrast meets WCAG AA
- [ ] Alt text on images/icons

---

## 🐛 Known Limitations

1. **Resource Downloads:**
   - Currently show alerts (not real downloads)
   - **Fix:** Connect to backend API

2. **Live Feed:**
   - Simulated data (not real signals)
   - **Fix:** Connect to lemlist Intent API

3. **Email Form:**
   - Shows alert → redirects (not real submission)
   - **Fix:** Connect to Mailchimp/ConvertKit

4. **95 Signals Missing:**
   - Section placeholder exists
   - **Fix:** Insert your existing 95 signals HTML

---

## ✅ Final Checks

### Before Launch:
- [ ] All links point to correct URLs
- [ ] UTM parameters working
- [ ] Mobile responsive on real devices
- [ ] No JavaScript errors in console
- [ ] Images load properly (SVG logo)
- [ ] Forms validate properly
- [ ] CTAs trackable in analytics

### Post-Launch Monitoring:
- [ ] Google Analytics events firing
- [ ] Conversion tracking active
- [ ] Email capture working
- [ ] No 404 errors
- [ ] Page load speed optimal

---

## 🆘 Troubleshooting

### Calculator Not Updating?
- Check browser console for JS errors
- Ensure sliders have proper event listeners
- Verify calculation functions defined

### Matrix Dots Not Appearing?
- Check SVG rendering support
- Verify `renderMatrix()` function called
- Inspect element for `#matrix-signals` content

### Quiz Stuck?
- Check `selectAnswer()` function
- Verify `currentQuestion` incrementing
- Check `quizData` array loaded

### Feed Not Updating?
- Verify `setInterval` running
- Check `updateFeed()` function
- Ensure `feedIndex` incrementing

---

**Last Updated:** October 19, 2024
**Status:** ✅ Ready for Testing
