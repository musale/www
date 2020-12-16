---
published: true
title: "Is Dark Mode Environmentally Friendly?"
description: "A periodical reminder that when it comes to many things related to energy and sustainability, intuition and common sense may be fooling us."
date: "2020-12-16"
category: essays
tags:
  - energy
  - technology
image:
  unsplash: "photo-1526324553550-133d260e7d60"
image_caption: "Golden Gate City Night lights crystal prism ball. @sanfrancisco, unsplash.com."
---

Dark mode is all the rage nowadays. Its benefits (or counter-intuitive lack thereof) have been widely discussed in various places of the web.

What I'd like to focus on in this small piece is this. Does dark mode have an effect on power usage? If I turn on dark mode on my mobile phone, or my laptop, will it "save battery life" — meaning, consume less electrical power overall? Could dark mode even be… environmentally friendly? 🌍

Well… not really. As for many things: it depends.

At first it might seem like a non-question. If the screen is darker, then it's emitting less light, and certainly that means less energy is consumed. Right? WRONG. (Well, sometimes at least.)

## Defining the terms

* Dark mode. A design practice that results in screens showing more dark areas than white ones.
* Environmentally friendly. GHG? Metals? Minerals? Water use? … Oftentimes, GHG only. Fine.

## A tale of screens

> IFIXIT: 63% drop in OLED screens. https://www.ifixit.com/News/16952/does-dark-mode-really-save-battery-on-your-phone

As I learned today, it turns out that whether dark mode reduces power usage depends on a variety of factors — in particular, screen technology.

Interestingly, this question is a portal towards entire areas of physics (optics, eletronics, semi-conductors). I'll try to give _some_ details since I've studied some of the physical mechanisms behind screen technologies during my engineering studies.

But first, the quick answer: If you're using an [LCD](https://en.wikipedia.org/wiki/Liquid-crystal_display) screen, then power usage isn't really affected by dark mode. For [OLED](https://en.wikipedia.org/wiki/OLED) screens though, power usage may indeed be reduced.

LCDs make up for most mobile phones today. So it's more likely than not that using dark mode on your mobile phone _won't_ save energy.

The main reason is that LCD screens use backlight to display images (pixels don't emit light by themselves). You can think of this as an always-on lamp in front of which you'd put some kind of filter to produce the desired colors, shapes, and intensities. Regardless of what comes out, the lamp is always-on — and so

The main reason is that in LCD screens the individual pixels don't emit light by themselves — they need a "backlight". When the screen is dark, pixels are set so that no light comes _out_, but the backlight is still on — and so power usage isn't really affected. On the other hand, individual pixels in OLED screens do emit light by themselves — they don't need a backlight. So when an OLED screen is dark, it's _really_ because pixels are literally _turned off_ — and so power usage is reduced.

For mobile phones, there are two big families of screen technologies: LCD and OLED. In short, LCDs LCDs use an "always-on" backlight, so the screen being white or dark doesn't actually change its power consumption much.

LCD stands for [_Liquid Crystal Display_](https://en.wikipedia.org/wiki/Liquid-crystal_display). An LCD screen consists in two parts: a [backlight](https://en.wikipedia.org/wiki/Backlight), which emits actual light, and [liquid crystals](https://en.wikipedia.org/wiki/Liquid_crystal), whose role is to _modulate_ that light so that it becomes colorized and of varying intensity. For mobile phones, the vast majority of LCD screens use an LED backlight, and more specifically "white" LEDs. (White light is achieved by associating a blue LED and a yellow-emitting material, such as phosphor, whose addition results in white light.)

## A word on environmental impacts of mobile devices

Even if dark mode _did_ contribute to reduce energy consumption from your device, the effects on sustainability would most likely be negligible. At least so unless you also pay attention to some other much more impactful aspects. Here's why.

Like virtually all consumer goods, a smartphone goes through a **lifecycle in 3 phases**: manufacturing, usage, and destruction. This distinction is at the basis of lifecycle analysis (LCA), which allows to understand the environmental impacts of a system over its entire life.

As it turns out, **most environmental impacts of mobile devices are located at the _manufacturing_ phase**. In other words, the usage phase only represents a small fraction. In fact, in terms of carbon emissions only the ratio is 80% or more at manufacturing, and 20% or less at usage. (This ratio notably depends on the carbon intensity of electricity, which can be anywhere between 60gCO2/kWh in countries like France or Sweden, to 400 gCO2/kWh or more in countries like the US or China.)

So the key driver of environmental impacts of smartphones the the sheer **production volume** (global smartphone production in 2019 was estimated to about 1.4 billion units [ref-needed]) — not so much how much electricity they use at runtime.

One of the key things we can do to help slow down production trends is **keeping our phones around for as long as we can**.

Wait, you want figures of how much more effective that is? 🙃 Okay, let's find out.

## Enter maths

Currently, the average replacement period of mobile phones in the EU is 2 years. If it was higher, then we'd need to produce less smartphones year on year, meaning less smartphones would be produced overall.

The custom graph graph of mine below\* (see [appendix](#manufacturing-impact-reduction-graph) for derivation details) shows that we could realistically achieve between 50% and 70% reduction (for a 4-year and 6-year replacement period respectively).

In comparison, the following table shows that dark mode can only bring a power usage reduction on OLED smartphones (since LCDs are backlit anyway), and that the reduction may be up to 60%. (This is obtained at maximum brightness, so it's _probably_ an optimistic figure — we might expect the reduction at lower brightness levels to be less — but I haven't found data to back that up.)

| Experiment | Pixel Current (mA) | iPhone7 Current (mA)|
|---|---|---|
| Max Brightness - Normal Mode | 250 | 230 |
| Max Brightness - Night Mode | 92 (-63%) | 230 (-0%) |

_**Table**: Compared power of Pixel (AMOLED) and iPhone 7 (LCD) displaying screenshot of Google Maps in normal and night mode. Source: [Cost of a pixel color](https://www.youtube.com/watch?v=N_6sPd0Jd3g&t=4m0s), Android Dev Summit 2018._

Let's combine this with the respective weights of manufacturing and usage. Since usage is only responsible for 20% of impacts, using dark mode on OLED devices can bring an improvement of at most 13% (virtually 0% for LCDs). Manufacturing is responsible for 80% of GHG impacts, so holding onto a smartphone for longer brings a realistic improvement between 40% (4-year replacement period) and 55% (6-year replacement period).

This leads us to the following summary table:

| Impact lever | Overall GHG impact reduction (LCA) |
|---|---|
| LCD dark mode (compared to light mode) | 0% |
| OLED dark mode (compared to light mode) | 12% |
| 4-year lifespan (ompared to 2-year) | 40% |
| 6-year lifespan (compared to 2-year) | 55% |

Overall, replacing a smartphone less often is at least effectively **3 to 4 times more impactful** than turning on dark mode for OLEDs (and **infinitely more effective** for LCDs).

Of course, these numbers only refer to greenhouse gas emissions. There are many other aspects to environmental impacts of smartphones — and consumer electronics in general — such as those related to the use of minerals and metals. I have no idea which of LCDs or OLEDs is more advantageous there, but it doesn't matter much. The take-away here I believe, is that the most impactful thing you can do as a smartphone user is keep your smartphone around longer.

That doesn't mean you shouldn't use dark mode, obviously. If you find it more aesthetic, more legible, and if it helps with eye strain in certain situations, then by all means, feel free to use it. But I guess what I take away from this deep-dive is this: let's not trick ourselves into thinking that it's an environmentally friendly thing to do — because that's not clear at all, and focusing on it at the expense of manufacturing impacts is bound to end up in a net-negative effect overall.

---

## Appendix

### Manufacturing impact reduction graph

The graph shows an estimation of the reduction of impacts associated to the manufacturing of smartphones plotted against the replacement period. It was derived as follows. We make a super-harsh simplification of reality, and assume that the individual impact of producing a smartphone is the same for every smartphone — some number `I_0`. If all smartphones are replaced after a period `T_r` (in years), then the annualized impact is `I_0 / T_r`. So the overall impact after `t` years is: `I_r(t) = (I_0 / T_r) * t`. To get the reduction compared to the current situation, which is a 2-year replacement period, we compute `R(t, T_r) = 100 * (I_2(t) - I_r(t)) / I_2(t)`, which gives the reduction in %. By replacing `I_2(t)` and `I_r(t)` by their formula and simplifying the expression, we get `R(t, T_r) = 100 * (1 - 2 / T_r)`, which actually only depends on `T_r`, the replacement period. The graph shows this expression of `R(T_r)` plotted against `T_r`.
